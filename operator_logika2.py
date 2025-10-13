nama = input("Masukkan Nama Anda: ")
motor = input("Apakah Anda memiliki motor? (yes/no): ").strip().lower() == 'yes'
SIM = input("Apakah Anda memiliki SIM? (yes/no): ").strip().lower() == 'yes'
umur = int(input("Masukkan umur Anda: "))

if motor and SIM and umur >= 17:
    print(f"{nama}, Anda boleh mengendarai motor.")
else:
    print(f"{nama}, Anda tidak boleh mengendarai motor.")