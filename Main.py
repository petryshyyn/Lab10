from Stadium import Stadium


def main():
    Stadium.security()
    football_stadium = Stadium(number_of_spectators=90_000, name_stadium="Camp_Nou", lighting_power_in_suites=9,
                               year_building=1957, country="Span", price=120_000_000)
    olympic_stadium = Stadium(number_of_spectators=60_000, lighting_power_in_suites=8,
                              country="England", price=100_000_000)
    american_football_stadium = Stadium(number_of_spectators=50_000, country="USA")

    football_stadium.__str__()
    olympic_stadium.__str__()
    american_football_stadium.__str__()


main()
