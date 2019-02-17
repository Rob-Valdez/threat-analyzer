# This is a threat analysis tool

def main():
    print_header()
    threats_list = create_threat()
    evaluated_threats_list = evaluate_threat(threats_list)
    print_results(evaluated_threats_list)


def print_header():
    print('------------------------------------------------------------------')
    print('                          Threat Analysis')
    print('------------------------------------------------------------------')
    print('')


def create_threat():
    threats_list = []
    active = True
    while active:
        message = input(
            '\n'
            'Enter a threat for analysis? [or enter \'y\' to enter a threat or enter \'n\' to quit]\n'
        ).strip().lower()
        if message == 'y':
            threat = {
                'name': input('What is the name of the threat?\n'),
                'category': input('What initiates this threat? [human, equipment, environment]\n'),
                'vector': input('What is the vector [pathway] of this threat?\n')
            }
            threats_list.append(threat)
        elif message == 'n':
            break
        else:
            print('That is not a valid option.')
    return threats_list


def evaluate_threat(threats_list):
    print('Let\'s evaluate the likelihood of each threat.')
    evaluated_threats_list = []
    for each in threats_list:
        print('\nThreat: ', end='')
        print(each['name'].title())
        each['likelihood'] = input('What is the likelihood of this threat?\n')
        evaluated_threats_list.append(each)
    return evaluated_threats_list


def print_results(evaluated_threat_list):
    print('\nHere are the results:')
    for each in evaluated_threat_list:
        print('')
        for k, v in each.items():
            print(f'{k}: {v}')


if __name__ == '__main__':
    main()
