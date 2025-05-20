class Character:

    next_id = 0

    def __init__(self):
        # Don't initialise this like this, use the factory method

        # Fields used officially
        self.id = ""
        self.name = ""
        self.team = ""
        self.ability = ""
        self.reminders = []
        self.jinxes = {}
        self.first_night = None
        self.other_nights = None
        self.first_night_reminder = ""
        self.other_nights_reminder = ""

        # Fields not used officially, but in other code in this repository
        self.overview = ""
        self.how_to_run = ""
        self.examples = []
        self.tip = ""
        self.preceedingOfficialCharacterId = ""

    def from_json(in_json):

        out_character = Character()

        id = in_json.get("id", None)
        if id is None:
            id = f"no_id_{Character.next_id}"
            Character.next_id += 1
        out_character.id = id

        name = in_json.get("name", "Unnamed")
        out_character.name = name

        team = in_json.get("team", "traveler") # I'm making traveller the default.
        out_character.team = team

        ability = in_json.get("ability", "You start knowing that the script writer forgot to put anything here.")
        out_character.ability = ability

        reminders = in_json.get("reminders", [])
        out_character.reminders = reminders

        jinxes = in_json.get("jinxes", [])
        new_jinxes = {}
        for jinx in jinxes:
            new_jinxes[jinx["id"]] = jinx["reason"]
        out_character.jinxes = new_jinxes

        first_night = in_json.get("firstNight", None)
        out_character.first_night = first_night

        other_nights = in_json.get("otherNights", None)
        out_character.other_nights = other_nights

        first_night_reminder = in_json.get("firstNightReminder", "")
        out_character.first_night_reminder = first_night_reminder

        other_nights_reminder = in_json.get("otherNightsReminder", "")
        out_character.other_nights_reminder = other_nights_reminder
