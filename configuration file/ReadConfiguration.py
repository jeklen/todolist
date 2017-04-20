import ConfigParser

config = ConfigParser.RawConfigParser()
try:
	config.read('example.cfg')

# getfloat() raises an exception if the value
# is not a float 
# gitint() and getboolean() also do this for 
# their respective types
	config.add_section('Secion2')
	config.set('Secion2', 'Qiaolun', 'Cool')
	a_float = config.getfloat('Secion1', 'a_float')
	an_int = config.getint('Secion1', 'an_int')
	print a_float + an_int

# Notice that the next output does not
# interpolate '%(bar)s' or '%(baz)s'.
# This is because we are using a RawConfigParser()

# to get interpolation, you will need to use a
# ConfigParser or SafeConfigParser:
	if config.getboolean('Secion1', 'a_bool'):
		print config.get('Secion1', 'foo')
	with open('example.cfg', 'wb') as configfile:
		config.write(configfile)
except ConfigParser.NoSectionError:
	print 1