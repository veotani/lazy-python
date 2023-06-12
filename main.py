print('Resources loading started')
import resources
from resources import eager
print('Resources loading finished')


print('Accessing lazy resource value')
assert resources.lazy.value == 'lazy'
print('Accessed lazy resource value')

print('Accessing eager value')
assert eager.value == 'eager'
print('Accessed eager value')
