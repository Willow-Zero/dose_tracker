# substances are listed with all-lowercase strings.
# substances have the following keys in their associated dictionaries:
#	life: their nalf life in hours.
#	 phrase as days*24 if the half life is measured in days.
#	 phrase as minutes/60.
#	 if the half life is measured in minutes.
#	 if its measured in seconds, phrase as seconds/60/60.
#	 this is not intended to cause confusion but to allow this
#	 document to be more human-readable.
substances = {
	"estradiol valerate":{"life":4.5*24},
	"estradiol cypionate":{"life":9*24}

}
