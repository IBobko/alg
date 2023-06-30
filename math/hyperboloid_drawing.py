import numpy as np
import matplotlib.pyplot as plt
import cart opy.crs as ccrs

def draw_geodesic_lines(latitude, longitude, num_lines, line_spacing):
    # Создание экземпляра карты
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # Параметры карты
    ax.coastlines()
    ax.stock_img()

    # Генерация координат для геодезических линий
    lats = np.linspace(latitude - line_spacing * (num_lines // 2), latitude + line_spacing * (num_lines // 2), num_lines)
    lons = np.repeat(longitude, num_lines)

    # Построение геодезических линий
    for lat, lon in zip(lats, lons):
        # Построение линии
        ax.plot([longitude, lon], [latitude, lat], 'r--', transform=ccrs.Geodetic())

    # Отображение карты
    plt.show()

# Пример использования
draw_geodesic_lines(latitude=40.7128, longitude=-74.0060, num_lines=5, line_spacing=1.0)
