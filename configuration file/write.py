import ConfigParser

config = ConfigParser.RawConfigParser()

# When adding sections or items, add them
# in the reverse order of how you want them 
# be displayed in the actual file,
# in addition, please note that using 
# RawConfigParser's and the raw mode of  
# ConfigParser's respective set functions, 
# you can assign non-string values to keys
# internally, but will receive an error
# when attempting to write to a file or when 
# you get it in non-raw mode. SafeConfigParser
# does not allow such assignments to take place.
config.add_section('Secion1')
config.set('Secion1', 'an_int')
config.set('Secion1', 'a_bool', 'true')
config.set('Secion1', 'a_float', '3.1415')
config.set('Secion1', 'baz', 'fun')
config.set('Secion1', 'bar', 'Python')
config.set('Secion1', 'foo', '%(bar)s is %(baz)s!')

# Writing our configuration file to 'example.cfg'
with open('example.cfg', 'wb') as configfile:
	config.write(configfile)