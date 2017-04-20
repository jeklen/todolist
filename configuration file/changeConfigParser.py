import ConfigParser

config = ConfigParser.ConfigParser()
config.read('example.cfg')

# Set the third, optional argument of get to
# 1 if you wish to use raw mode.
print config.get('Secion1', 'foo', 0)
print config.get('Secion1', 'foo', 1)
print config.get('Secion1', 'foo', 0, {'bar':'Documentation','baz':'evil'})