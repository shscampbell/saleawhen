from flask import render_template, request
from saleawhen import app
from saleawhen import sale_model

communities = [
    "", "01F", "01G", "05D", "06A", "09K", "12A", "12B", "12C", "12J", "13K",
    "Abbeydale", "Acadia", "Alberta Park/Radisson Heights", "Altadore",
    "Alyth/Bonnybrook", "Applewood Park", "Arbour Lake", "Aspen Woods",
    "Auburn Bay", "Aurora Business Paprk", "Banff Trail", "Bankview",
    "Bayview", "Beddington Heights", "Bel-Aire", "Belmont", "Beltline",
    "Belvedere", "Bonavista Downs", "Bowness", "Braeside", "Brentwood",
    "Bridgeland/Riverside", "Bridlewood", "Britannia", "Burns Industrial",
    "Calgary International Airport", "Cambrian Heights", "Canyon Meadows",
    "Capitol Hill", "Carrington", "Castleridge", "Cedarbrae", "Chaparral",
    "Charleswood", "Chinatown", "Chinook Park", "Christie Park", "Citadel",
    "Cityscape", "Cliff Bungalow", "Coach Hill", "Collingwood", "Copperfield",
    "Coral Springs", "Cornerstone", "Cougar Ridge", "Country Hills",
    "Country Hills Village", "Coventry Hills", "Cranston", "Crescent Heights",
    "Crestmont", "Currie Barracks", "Dalhousie", "Deer Ridge", "Deer Run",
    "Deerfoot Business Centre", "Diamond Cove", "Discovery Ridge",
    "Douglasdale/Glen", "Dover", "Downtown Commercial Core",
    "Downtown East Village", "Downtown West End", "Eagle Ridge",
    "East Fairview Industrial", "East Shepard Industrial", "Eastfield",
    "Eau Claire", "Edgemont", "Elbow Park", "Elboya", "Erin Woods", "Erlton",
    "Evanston", "Evergreen", "Fairview", "Fairview Industrial", "Falconridge",
    "Fish Creek Park", "Foothills", "Forest Heights", "Forest Lawn",
    "Forest Lawn Industrial", "Garrison Green", "Garrison Woods", "Glamorgan",
    "Glenbrook", "Glendale", "Greenview", "Greenview Industrial Park",
    "Hamptons", "Harvest Hills", "Hawkwood", "Haysboro", "Hidden Valley",
    "Highfield", "Highland Park", "Highwood", "Hillhurst", "Horizon",
    "Hounsfield Heights/Briar Hill", "Huntington Hills", "Inglewood",
    "Kelvin Grove", "Killarney/Glengarry", "Kincora", "Kingsland",
    "Lake Bonavista", "Lakeview", "Legacy", "Lincoln Park", "Livingston",
    "Lower Mount Royal", "Macewan Glen", "Mahogany", "Manchester",
    "Manchester Industrial", "Maple Ridge", "Marlborough", "Marlborough Park",
    "Martindale", "Mayfair", "Mayland Heights", "McCall", "McKenzie Lake",
    "McKenzie Towne", "Meadowlark Park", "Meridian", "Midnapore", "Millrise",
    "Mission", "Monterey Park", "Montgomery", "Mount Pleasant", "New Brighton",
    "Nolan HIll", "North Airways", "North Glenmore Park", "North Haven",
    "North Haven Upper", "Nose Hill Park", "Oakridge", "Ogden", "Palliser",
    "Panorama Hills", "Parkdale", "Parkdale", "Parkhill", "Parkland",
    "Patterson", "Penbrooke Meadows", "Pineridge", "Point McKay", "Pump Hill",
    "Queensland", "Ramsay", "Ranchlands", "Red Carpet", "Redstone", "Renfrew",
    "Richmond", "Rideau Park", "Rocky Ridge", "Rosedale", "Rosemont",
    "Rosscarrock", "Roxboro", "Royal Oak", "Royal Vista", "Rundle",
    "Rutland Park", "Saddle Ridge", "Sage Hill", "Sandstone Valley",
    "Scarboro", "Scarboro/Sunalta West", "Scenic Acres", "Seton", "Shaganappi",
    "Shawnee Slopes", "Shawnessy", "Shepard Industrial", "Sherwood",
    "Signal Hill", "Silver Springs", "Silverado", "Skyline East",
    "Skyview Ranch", "Somerset", "South Airways", "South Calgary",
    "Southview", "Southwood", "Springbank Hill", "Spruce Cliff",
    "St. Andrews Heights", "Starfield", "Stoney 1", "Strathcona Park",
    "Sunalta", "Sundance", "Sunnyside", "Sunridge", "Taradale", "Temple",
    "Thorncliffe", "Tuscany", "Tuxedo Park", "University District",
    "University Heights", "Upper Mount Royal", "Valley Ridge", "Valleyfield",
    "Varsity", "Vista Heights", "Walden", "West Hillhurst", "West Springs",
    "Westgate", "Westwinds", "Whitehorn", "Wildwood", "Willow Park",
    "Windsor Park", "Winston Heights/Mountview", "Woodbine", "Woodlands"]

# The Flask class has a method called route that takes a string (representing a
# path) and returns a decorator that defines a routine (called serve) that
# causes my function askawhen_index() to be called when serve("/") is called.
# i.e., it registers my "view function" with the route "/" so that whenever
# there is a request to the "/" route, this view function will be invoked and
# its result will be sent back to the client.


@app.route("/")
@app.route("/index")
def askawhen_index():
    return render_template("form/form.html")


@app.route("/results")
def askawhen_result():
    # Get the data from the submitted form.
    # The month when the listing is posted.
    month = request.args.get('month')
    # The listed community.
    comm = request.args.get('community')
    # The number of bedrooms.
    br = request.args.get('brs')
    # The number of bedrooms above ground.
    brag = request.args.get('brags')
    # The number of full bathrooms
    bath = request.args.get('baths')
    # The number of half bathrooms
    hbath = request.args.get('hbaths')
    # The square footage of the home.
    sqft = request.args.get('sqft')
    # The annual property tax on the home.
    tax = request.args.get('tax')
    # The age of the home in years.
    age = request.args.get('age')
    # Is the home an apartment?
    isapt = request.args.get('prop_apt')
    # Is the home in a flood zone?
    isflood = request.args.get('prop_flood')
    # Is the property fenced?
    isfence = request.args.get('prop_fence')
    # Does the home contain a hot tub?
    ishottub = request.args.get('prop_hottub')
    # Does the home come with window coverings?
    iscurts = request.args.get('prop_curts')
    # Does the home have vinyl siding?
    isvinyl = request.args.get('prop_vinyl')
    # Does the home have non-ceramic tile flooring?
    isnctile = request.args.get('prop_floor')
    # The requested quantile of the survival function.
    quantile = request.args.get('conflevel')

    if isapt is None:
        isapt = 0
        aptchecked = ""
    else:
        isapt = 1
        aptchecked = "checked"
    if isflood is None:
        isflood = 0
        floodchecked = ""
    else:
        isflood = 1
        floodchecked = "checked"
    if isfence is None:
        isfence = 0
        fencechecked = ""
    else:
        isfence = 1
        fencechecked = "checked"
    if ishottub is None:
        ishottub = 0
        hottubchecked = ""
    else:
        ishottub = 1
        hottubchecked = "checked"
    if iscurts is None:
        iscurts = 0
        curtschecked = ""
    else:
        iscurts = 1
        curtschecked = "checked"
    if isvinyl is None:
        isvinyl = 0
        vinylchecked = ""
    else:
        isvinyl = 1
        vinylchecked = "checked"
    if isnctile is None:
        isnctile = 0
        nctilechecked = ""
    else:
        isnctile = 1
        nctilechecked = "checked"

    if brag > br:
        message = 'Error: The number of bedrooms above ground is greater ' + \
            'than the total number of bedrooms.'
    else:
        # Calculate the expected sale time.
        sale = sale_model.saletimeCalgary(
            month, brag, bath, sqft, tax, age, isapt,
            isflood, isfence, ishottub, iscurts,
            isvinyl, isnctile, quantile)
        message = F'This listing is {quantile}% likely to sell ' + \
            F'in {sale} days.'
    return render_template(
        "form/form2.html", message=message, month=month,
        comm=comm, community=communities[int(comm)], br=br, brag=brag,
        bath=bath, hbath=hbath, sqft=sqft, tax=tax, age=age,
        aptchecked=aptchecked, floodchecked=floodchecked,
        fencechecked=fencechecked, hottubchecked=hottubchecked,
        curtschecked=curtschecked, vinylchecked=vinylchecked,
        nctilechecked=nctilechecked, conflevel=quantile)
