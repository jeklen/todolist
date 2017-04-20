import ConfigParser

config = ConfigParser.SafeConfigParser({'bar':'Life', 'baz':'hard'})
config.read('example.cfg')

print config.get('Secion1', 'foo')
config.remove_option('Secion1', 'bar')
config.remove_option('Secion1', 'baz')
print config.get('Secion1', 'foo')