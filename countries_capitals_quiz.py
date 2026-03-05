# My first project - Country to Capital
# This program will do a variety of tasks, such as: Asking the user to match a capital with a randomly selected country, allowing the user to input a country and outputting the capital and also doing the opposite for each task.
# Patrick Walker - 16/02/2026

import random

# Create a dictionary of countries and their capitals
countries_and_capitals = {
    "AFGHANISTAN": "KABUL",
"ALBANIA": "TIRANA",
"ALGERIA": "ALGIERS",
"ANDORRA": "ANDORRA LA VELLA",
"ANGOLA": "LUANDA",
"ANTIGUA & BARBUDA": "SAINT JOHN'S",
"ARGENTINA": "BUENOS AIRES",
"ARMENIA": "YEREVAN",
"AUSTRALIA": "CANBERRA",
"AUSTRIA": "VIENNA",
"AZERBAIJAN": "BAKU",
"THE BAHAMAS": "NASSAU",
"BAHRAIN": "MANAMA",
"BANGLADESH": "DHAKA",
"BARBADOS": "BRIDGETOWN",
"BELARUS": "MINSK",
"BELGIUM": "BRUSSELS",
"BELIZE": "BELMOPAN",
"BENIN": "PORTO-NOVO",
"BHUTAN": "THIMPHU",
"BOLIVIA": ["SUCRE", "LA PAZ"],
"BOSNIA & HERZEGOVINA": "SARAJEVO",
"BOTSWANA": "GABORONE",
"BRAZIL": "BRASILIA",
"BRUNEI": "BANDAR SERI BEGAWAN",
"BULGARIA": "SOFIA",
"BURKINA FASO": "OUAGADOUGOU",
"BURUNDI": ["GITEGA", "BUJUMBURA"],
"CABO VERDE": "PRAIA",
"CAMBODIA": "PHNOM PENH",
"CAMEROON": "YAOUNDE",
"CANADA": "OTTAWA",
"CENTRAL AFRICAN REPUBLIC": "BANGUI",
"CHAD": "N'DJAMENA",
"CHILE": "SANTIAGO",
"CHINA": "BEIJING",
"COLOMBIA": "BOGOTA",
"COMOROS": "MORONI",
"CONGO (DEMOCRATIC REPUBLIC)": "KINSHASA",
"CONGO (REPUBLIC)": "BRAZZAVILLE",
"COSTA RICA": "SAN JOSE",
"COTE D'IVOIRE": "YAMOUSSOUKRO",
"CROATIA": "ZAGREB",
"CUBA": "HAVANA",
"CYPRUS": "NICOSIA",
"CZECHIA": "PRAGUE",
"DENMARK": "COPENHAGEN",
"DJIBOUTI": "DJIBOUTI",
"DOMINICA": "ROSEAU",
"DOMINICAN REPUBLIC": "SANTO DOMINGO",
"ECUADOR": "QUITO",
"EGYPT": "CAIRO",
"EL SALVADOR": "SAN SALVADOR",
"EQUATORIAL GUINEA": "CIUDAD DE LA PAZ",
"ERITREA": "ASMARA",
"ESTONIA": "TALLINN",
"ESWATINI": "MBABANE",
"ETHIOPIA": "ADDIS ABABA",
"FIJI": "SUVA",
"FINLAND": "HELSINKI",
"FRANCE": "PARIS",
"GABON": "LIBREVILLE",
"GAMBIA": "BANJUL",
"GEORGIA": "TBILISI",
"GERMANY": "BERLIN",
"GHANA": "ACCRA",
"GREECE": "ATHENS",
"GRENADA": "SAINT GEORGE'S",
"GUATEMALA": "GUATEMALA CITY",
"GUINEA": "CONAKRY",
"GUINEA-BISSAU": "BISSAU",
"GUYANA": "GEORGETOWN",
"HAITI": "PORT-AU-PRINCE",
"HONDURAS": "TEGUCIGALPA",
"HUNGARY": "BUDAPEST",
"ICELAND": "REYKJAVIK",
"INDIA": "NEW DELHI",
"INDONESIA": "JAKARTA",
"IRAN": "TEHRAN",
"IRAQ": "BAGHDAD",
"IRELAND": "DUBLIN",
"ISRAEL": "JERUSALEM",
"ITALY": "ROME",
"JAMAICA": "KINGSTON",
"JAPAN": "TOKYO",
"JORDAN": "AMMAN",
"KAZAKHSTAN": "ASTANA",
"KENYA": "NAIROBI",
"KIRIBATI": "SOUTH TARAWA",
"KOSOVO": "PRISTINA",
"KUWAIT": "KUWAIT CITY",
"KYRGYZSTAN": "BISHKEK",
"LAOS": "VIENTIANE",
"LATVIA": "RIGA",
"LEBANON": "BEIRUT",
"LESOTHO": "MASERU",
"LIBERIA": "MONROVIA",
"LIBYA": "TRIPOLI",
"LIECHTENSTEIN": "VADUZ",
"LITHUANIA": "VILNIUS",
"LUXEMBOURG": "LUXEMBOURG CITY",
"MADAGASCAR": "ANTANANARIVO",
"MALAWI": "LILONGWE",
"MALAYSIA": "KUALA LUMPUR",
"MALDIVES": "MALE",
"MALI": "BAMAKO",
"MALTA": "VALLETTA",
"MARSHALL ISLANDS": "MAJURO",
"MAURITANIA": "NOUAKCHOTT",
"MAURITIUS": "PORT LOUIS",
"MEXICO": "MEXICO CITY",
"FEDERATED STATES OF MICRONESIA": "PALIKIR",
"MOLDOVA": "CHISINAU",
"MONACO": "MONACO",
"MONGOLIA": "ULAANBAATAR",
"MONTENEGRO": "PODGORICA",
"MOROCCO": "RABAT",
"MOSAMBIQUE": "MAPUTO",
"MYANMAR": "NAYPYIDAW",
"NAMIBIA": "WINDHOEK",
"NEPAL": "KATHMANDU",
"NETHERLANDS": "AMSTERDAM",
"NEW ZEALAND": "WELLINGTON",
"NICARAGUA": "MANAGUA",
"NIGER": "NIAMEY",
"NIGERIA": "ABUJA",
"NORTH KOREA": "PYONGYANG",
"NORTH MACEDONIA": "SKOPJE",
"NORWAY": "OSLO",
"OMAN": "MUSCAT",
"PAKISTAN": "ISLAMABAD",
"PALAU": "NGERULMUD",
"PALESTINE": "EAST JERUSALEM",
"PANAMA": "PANAMA CITY",
"PAPUA NEW GUINEA": "PORT MORESBY",
"PARAGUAY": "ASUNCION",
"PERU": "LIMA",
"PHILIPPINES": "MANILA",
"POLAND": "WARSAW",
"PORTUGAL": "LISBON",
"QATAR": "DOHA",
"ROMANIA": "BUCHAREST",
"RUSSIA": "MOSCOW",
"RWANDA": "KIGALI",
"SAINT KITTS & NEVIS": "BASSETERRE",
"SAINT LUCIA": "CASTRIES",
"SAINT VINCENT & THE GRENADINES": "KINGSTOWN",
"SAMOA": "APIA",
"SAN MARINO": "SAN MARINO",
"SÃO TOMÉ & PRÍNCIPE": "SÃO TOMÉ",
"SAUDI ARABIA": "RIYADH",
"SENEGAL": "DAKAR",
"SERBIA": "BELGRADE",
"SEYCHELLES": "VICTORIA",
"SIERRA LEONE": "FREETOWN",
"SINGAPORE": "SINGAPORE",
"SLOVAKIA": "BRATISLAVA",
"SLOVENIA": "LJUBLJANA",
"SOLOMON ISLANDS": "HONIARA",
"SOMALIA": "MOGADISHU",
"SOUTH AFRICA": ["PRETORIA", "CAPE TOWN", "BLOEMFONTEIN"],
"SOUTH KOREA": "SEOUL",
"SOUTH SUDAN": "JUBA",
"SPAIN": "MADRID",
"SRI LANKA": ["COLOMBO", "SRI JAYAWARDENEPURA KOTTE"],
"SUDAN": "KHARTOUM",
"SURINAME": "PARAMARIBO",
"SWEDEN": "STOCKHOLM",
"SWITZERLAND": "BERN",
"SYRIA": "DAMASCUS",
"TAIWAN": "TAIPEI",
"TAJIKISTAN": "DUSHANBE",
"TANZANIA": "DODOMA",
"THAILAND": "BANGKOK",
"TIMOR-LESTE": "DILI",
"TOGO": "LOME",
"TONGA": "NUKU'ALOFA",
"TRINIDAD & TOBAGO": "PORT OF SPAIN",
"TUNISIA": "TUNIS",
"TURKEY": "ANKARA",
"TURKMENISTAN": "ASHGABAT",
"TUVALU": "FUNAFUTI",
"UGANDA": "KAMPALA",
"UKRAINE": "KYIV",
"UNITED ARAB EMIRATES": "ABU DHABI",
"UNITED KINGDOM": "LONDON",
"UNITED STATES": "WASHINGTON, D.C.",
"URUGUAY": "MONTEVIDEO",
"UZBEKISTAN": "TASHKENT",
"VANUATU": "PORT VILA",
"VATICAN CITY": "VATICAN CITY",
"VENEZUELA": "CARACAS",
"VIETNAM": "HANOI",
"YEMEN": "SANA'A",
"ZAMBIA": "LUSAKA",
"ZIMBABWE": "HARARE"
}


def get_capital():
    # Ask the user to input a country
    country = input("Enter a country: ").upper()
    # Check if the country is in the dictionary
    try:
        if isinstance(countries_and_capitals[country], list):
            print(f"The capital of {country} is either {' or '.join(countries_and_capitals[country])}")
        elif isinstance(countries_and_capitals[country], str):
            print(f"The capital of {country} is {countries_and_capitals[country]}")
    except KeyError:
        print(f"Sorry, that country isn't in the dictionary.")
    # Ask the user if they would like another capital
    def another_capital():
        another = input("Would you like to look up another capital? (yes/no) ").lower()
        if another == "yes":
            get_capital()
        elif another == "no":
            print("Goodbye! Try having a go at the quiz to test your knowledge of capitals!")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    another_capital()


def quiz_user():
    # Ask the user how many questions they want to answer
    num_questions = int(input("How many questions would you like to answer? "))
    for _ in range(num_questions):
        # Randomly select a country and its capital
        country, capital = random.choice(list(countries_and_capitals.items()))
        # Ask the user to match the capital with the country
        user_input = input(f"What is the capital of {country}? ").upper()
        # Check if the user's answer is correct
        if isinstance(capital, list):
            if user_input in capital:
                print("Correct!")
            else:
                print(f"Wrong! The capital of {country} is {' or '.join(capital)}.")
        else:
            if user_input == capital:
                print("Correct!")
            else:
                print(f"Wrong! The capital of {country} is {capital}.")

def main():
    while True:
        print("Welcome to the countries and capitals quiz, what would you like to use the program for?")
        print("1. Get the capital of a country")
        print("2. Quiz yourself on capitals")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            get_capital()
        elif choice == "2":
            quiz_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()