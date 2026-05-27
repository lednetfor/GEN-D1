import os
import matplotlib.pyplot as plt

STORAGE_DIR = "/content/drive/MyDrive/bin/DN-35gmx/STORAGE"
_secret_pin = ["1234"] 

if not os.path.exists(STORAGE_DIR): 
    os.makedirs(STORAGE_DIR)

MAP_DNA = {'00': 'A', '01': 'T', '10': 'C', '11': 'G'}

def check_pin(user_pin):
    return user_pin == _secret_pin[0]

def set_pin(new_pin):
    _secret_pin[0] = new_pin

def get_storage_dir():
    return STORAGE_DIR

# معادلة التشفير الجيني السرية (مغلقة تماماً)
def gmx_encode(source, password):
    with open(source, 'rb') as f: data = bytearray(f.read())
    key = password.encode()
    encrypted = bytearray([b ^ key[i % len(key)] for i, b in enumerate(data)])
    
    dna_list = []
    for b in encrypted:
        b_str = bin(b)[2:].zfill(8)
        dna_list.append("".join([MAP_DNA[b_str[i:i+2]] for i in range(0, 8, 2)]))
    dna = "".join(dna_list)
    
    with open(os.path.join(STORAGE_DIR, f"{source}.gmx"), 'w') as f: f.write(dna)
    print(f"✅ Encodage ADN réussi : {source}.gmx")

def show_centura(source_gmx):
    with open(os.path.join(STORAGE_DIR, source_gmx), 'r') as f: dna = f.read()
    clean_dna = dna.replace('\n', '').replace('\r', '')
    mrna = clean_dna.replace('T', 'U')
    mapping = {'A': 1, 'U': 2, 'C': 3, 'G': 4}
    data = [mapping.get(b, 0) for b in mrna[:200]]
    plt.figure(figsize=(10, 2))
    plt.plot(data, 'o-', color='#800080')
    plt.title("GMX-mRNA-CENTURA: Molecular Portrait")
    plt.yticks([1, 2, 3, 4], ['A', 'U', 'C', 'G'])
    plt.show()
