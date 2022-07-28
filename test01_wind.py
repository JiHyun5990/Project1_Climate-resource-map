from netCDF4 import Dataset
import matplotlib.pyplot as plt

ncfile = Dataset('KMAPP_wind_10m_00H_mean.nc')
print(ncfile)

'''
<class 'netCDF4._netCDF4.Dataset'>
root group (NETCDF4 data model, file format HDF5):
    dimensions(sizes): X(6900), Y(6750)
    variables(dimensions): float64 X(X), float64 Y(Y), float32 windspeed(Y, X)
    groups: 
'''

windspeed = ncfile.variables['windspeed']

plt.imshow(windspeed)
plt.gca().invert_yaxis()
plt.colorbar()
plt.title('wind_00H')

plt.savefig('wind_00H.png')
plt.show()