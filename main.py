from snackification import snackify_meal
from processXML import import_xml_to_text
from gooey import Gooey, GooeyParser
from datetime import datetime

@Gooey(program_name='GovSnacks', tabbed_groups=True, image_dir='icons',header_height=200,  default_size=(750, 650),)
def main():
    parser = GooeyParser(description="\nTransform copious Australian Parliament House\nproceedings into bite-sized easily-digestible snacks\n\nDemo outputs available at GovSnacks.com.\n\nEnter your own OpenAI API Key in the advanced settings")

    group1 = parser.add_argument_group('Settings')

    # Date picker for selecting the start of a week
    group1.add_argument(
        '--week_start_date',
        metavar='Parliament Sitting Week',
        help='Select start of parliament sitting week',
        widget='DateChooser',  # Gooey widget for date picker
        default="19 Aug 2024 - 26 Aug 2024",

    )

    # Document selection using a dropdown menu
    group1.add_argument(
        'document',
        metavar='Select Document',
        help='Choose a document to summarise',
        choices=['19 Aug 2024 - Senate',
                 '19 Aug 2024 - House of Representatives',
                 '20 Aug 2024 - House of Representatives',
                 '20 Aug 2024 - Senate',
                 '21 Aug 2024 - House of Representatives',
                 '21 Aug 2024 - Senate', '22 Aug 2024 - Senate',
                 '22 Aug 2024 - House of Representatives'],  # Predefined document list
        widget='Dropdown'  # Gooey widget for dropdown selection
    )

    group1.add_argument(
        '--issues_of_interest',
        metavar='Issues of Interest',
        help='Focus the summary on your topics of interest (eg. \'disability rights\', \'gender equity\', \'immigration\', \'democracy taskforce\')',
        default='',  # Optional: Default value if any
        type=str,
        nargs = '+',  # Make the field optional
    )

    group2 = parser.add_argument_group('Advanced')

    # API Key input field
    group2.add_argument(
        'api_key',
        metavar='OpenAI API Key',
        help='Enter your OpenAI API key, available at https://platform.openai.com/api-keys',
        widget='TextField',
        default = ''
    )

    args = parser.parse_args()

    # Convert issues_of_interest to a single string if it's not empty
    if args.issues_of_interest:
        issues_of_interest = ' '.join(args.issues_of_interest)
    else:
        issues_of_interest = ''

    if args.issues_of_interest:
        print (f"\nSummarising \"{args.document}\" proceedings with a focus on \"{issues_of_interest}\"...\n")
    else:
        print(f"\nSummarising \"{args.document}\" proceedings... \n")

    document_map = {
        '19 Aug 2024 - Senate': 'doc1.xml',
        '19 Aug 2024 - House of Representatives': 'doc2.xml',
        '20 Aug 2024 - House of Representatives': 'doc3.xml',
        '20 Aug 2024 - Senate': 'doc4.xml',
        '21 Aug 2024 - House of Representatives': 'doc5.xml',
        '21 Aug 2024 - Senate': 'doc6.xml',
        '22 Aug 2024 - Senate': 'doc7.xml',
        '22 Aug 2024 - House of Representatives': 'doc8.xml'
    }

    # Use the selected document to get the corresponding XML file
    selected_option = args.document
    xml_file = document_map.get(selected_option)

    document = import_xml_to_text(f"docs/{xml_file}")

    print( snackify_meal(document, args.api_key, issues_of_interest))

if __name__ == '__main__':
    main()