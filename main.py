print('Resource loading started')
import loads_lazily
print('Resource loading finished')


print('Accessing resource value')
print(f'Value = {loads_lazily.resource.value}')
print('Accessed resource value')
