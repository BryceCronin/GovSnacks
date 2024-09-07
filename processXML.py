import xml.etree.ElementTree as ET

def estimate_token_count(text):
    # Basic approximation: 1 token is roughly 4 characters for English text
    return len(text) // 4

def import_xml_to_text(file_path, token_limit=100000):
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Initialize variables
        text_accumulated = ""
        current_token_count = 0

        # Traverse the XML and accumulate text until reaching the token limit
        for elem in root.iter():
            if elem.text:
                text_content = elem.text.strip()
                text_accumulated += text_content + " "

                # Estimate token count
                current_token_count = estimate_token_count(text_accumulated)

                # Stop if we exceed the token limit
                if current_token_count >= token_limit:
                    break

        return text_accumulated
    except Exception as e:
        print("An error occurred while trimming the XML file:", e)
        return None