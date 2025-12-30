import quopri
import re
import sys
import os

def decode_qp(text):
    try:
        # Remove the = at the end if it exists (soft line break in QP)
        # But quopri.decodestring handles it if it's a valid QP string.
        # However, in VCard, the value might be split across lines.
        # We will handle joining before calling this.
        decoded_bytes = quopri.decodestring(text.encode('utf-8'))
        return decoded_bytes.decode('utf-8').replace('\r\n', '').replace('\n', '').replace('\r', '')
    except Exception as e:
        print(f"Error decoding: {text} - {e}")
        return text

def parse_vcard_2_1(file_path):
    contacts = []
    current_contact = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if line == 'BEGIN:VCARD':
            current_contact = {'tels': []}
        elif line == 'END:VCARD':
            if current_contact:
                contacts.append(current_contact)
            current_contact = {}
        elif line.startswith('N;') or line.startswith('N:'):
            # Handle Name
            # Check for QP
            is_qp = 'ENCODING=QUOTED-PRINTABLE' in line
            
            # Get the value part
            if ':' in line:
                parts = line.split(':', 1)
                key_params = parts[0]
                value = parts[1]
                
                # Handle multi-line QP
                if is_qp:
                    while value.endswith('='):
                        i += 1
                        if i < len(lines):
                            next_line = lines[i].strip()
                            value = value[:-1] + next_line
                        else:
                            break
                    value = decode_qp(value)
                
                current_contact['n'] = value
        
        elif line.startswith('FN;') or line.startswith('FN:'):
            # Handle Formatted Name
            is_qp = 'ENCODING=QUOTED-PRINTABLE' in line
            
            if ':' in line:
                parts = line.split(':', 1)
                value = parts[1]
                
                if is_qp:
                    while value.endswith('='):
                        i += 1
                        if i < len(lines):
                            next_line = lines[i].strip()
                            value = value[:-1] + next_line
                        else:
                            break
                    value = decode_qp(value)
                
                current_contact['fn'] = value
                
        elif line.startswith('TEL;'):
            # Handle Phone
            # TEL;CELL:096 067 1949
            if ':' in line:
                parts = line.split(':', 1)
                meta = parts[0]
                number = parts[1]
                
                # Extract type if possible, default to CELL if not specified but usually it is
                tel_type = 'CELL'
                upper_meta = meta.upper()
                if 'HOME' in upper_meta: tel_type = 'HOME'
                elif 'WORK' in upper_meta: tel_type = 'WORK'
                elif 'MAIN' in upper_meta: tel_type = 'MAIN'
                elif 'FAX' in upper_meta: tel_type = 'FAX'
                elif 'OTHER' in upper_meta: tel_type = 'OTHER'
                
                current_contact['tels'].append({'number': number, 'type': tel_type})
                
        i += 1
        
    return contacts

def write_vcard_3_0(contacts, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            for c in contacts:
                f.write('BEGIN:VCARD\n')
                f.write('VERSION:3.0\n')
                
                if 'n' in c:
                    f.write(f"N:{c['n']}\n")
                else:
                    # Fallback if N is missing but FN exists
                    if 'fn' in c:
                        parts = c['fn'].split(' ')
                        if len(parts) > 1:
                            f.write(f"N:{parts[-1]};{' '.join(parts[:-1])};;;\n")
                        else:
                            f.write(f"N:{c['fn']};;;;\n")
                
                if 'fn' in c:
                    f.write(f"FN:{c['fn']}\n")
                
                for tel in c['tels']:
                    # Clean number? iOS is usually fine with spaces, but let's keep it as is.
                    f.write(f"TEL;TYPE={tel['type']}:{tel['number']}\n")
                
                f.write('END:VCARD\n')
    except IOError as e:
        print(f"Error writing to file {output_path}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_contacts.py <input_file.vcf>")
        print("Example: python convert_contacts.py contacts3.vcf")
        sys.exit(1)

    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    # Generate output filename: input_ios.vcf
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}_ios.vcf"

    print(f"Reading from {input_file}...")
    try:
        contacts = parse_vcard_2_1(input_file)
    except Exception as e:
        print(f"Error parsing file: {e}")
        sys.exit(1)

    if not contacts:
        print("Warning: No contacts found in the input file.")
    else:
        print(f"Found {len(contacts)} contacts.")
        print(f"Writing to {output_file}...")
        write_vcard_3_0(contacts, output_file)
        print("Done.")
