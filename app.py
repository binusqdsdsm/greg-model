from flask import Flask, render_template, url_for, request, redirect
import dsmSalary as modelSalary

app = Flask(__name__)

class PersonalInformation:
    def __init__(self, umur, status_pernikahan, jumlah_tanggungan, jarak_rumah, pendidikan_terakhir, total_personal_information):
        self.umur = umur
        self.status_pernikahan = status_pernikahan
        self.jumlah_tanggungan = jumlah_tanggungan
        self.jarak_rumah = jarak_rumah
        self.pendidikan_terakhir = pendidikan_terakhir
        self.total_personal_information = total_personal_information

class Skills:
    def __init__(self, pengetahuan, kemampuan, kecepatan, kualitas, jumlah, total_skills):
        self.pengetahuan = pengetahuan
        self.kemampuan = kemampuan
        self.kecepatan = kecepatan
        self.kualitas = kualitas
        self.jumlah = jumlah
        self.total_skills = total_skills

class Attitude:
    def __init__(self, perilaku, disiplin, kejujuran, tanggung_jawab, total_attitude):
        self.perilaku = perilaku
        self.disiplin = disiplin
        self.kejujuran = kejujuran
        self.tanggung_jawab = tanggung_jawab
        self.total_attitude = total_attitude

class Achievement:
    def __init__(self, pencapaian, pengalaman_bekerja, gaji, level_pekerjaan, total_achievement):
        self.pencapaian = pencapaian
        self.pengalaman_bekerja = pengalaman_bekerja
        self.gaji = gaji
        self.level_pekerjaan = level_pekerjaan
        self.total_achievement = total_achievement

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def resultGreg():
    final_result = False
    if request.method == 'POST':
        # PERSONAL INFORMATION
        umur = float(request.form['umur'])
        status_pernikahan = float(request.form['status_pernikahan'])
        jumlah_tanggungan = float(request.form['jumlah_tanggungan'])
        jarak_rumah = float(request.form['jarak_rumah'])
        pendidikan_terakhir = float(request.form['pendidikan_terakhir'])

        married_status = 'Belum Menikah'
        if status_pernikahan == 0:
            married_status = 'Belum Menikah'
        else:
            married_status = 'Sudah Menikah'

        edu_status = 'SD'
        if pendidikan_terakhir == 1:
            edu_status = 'SD'
        elif  pendidikan_terakhir == 2:
            edu_status = 'SMP'
        elif  pendidikan_terakhir == 3:
            edu_status = 'SMA/SMK'
        elif  pendidikan_terakhir == 4:
            edu_status = 'D3'
        elif  pendidikan_terakhir == 5:
            edu_status = 'S1'
        elif  pendidikan_terakhir == 6:
            edu_status = 'S2'
        elif  pendidikan_terakhir == 7:
            edu_status = 'S3'

        total_personal_information = modelSalary.personalInformation(umur, status_pernikahan, jumlah_tanggungan, jarak_rumah, pendidikan_terakhir)
        pi_1 = PersonalInformation(int(umur), married_status, int(jumlah_tanggungan), jarak_rumah, edu_status, total_personal_information)
        

        # # SKILLS
        pengetahuan = float(request.form['pengetahuan'])
        kemampuan = float(request.form['kemampuan'])
        kecepatan = float(request.form['kecepatan'])
        kualitas = float(request.form['kualitas'])
        jumlah = float(request.form['jumlah'])

        total_skills = modelSalary.skills(pengetahuan, kemampuan, kecepatan, kualitas, jumlah)
        s_1 = Skills(pengetahuan, kemampuan, kecepatan, kualitas, jumlah, total_skills)

        # ATTITUDE
        perilaku = float(request.form['perilaku'])
        disiplin = float(request.form['disiplin'])
        kejujuran = float(request.form['kejujuran'])
        tanggung_jawab = float(request.form['tanggung_jawab'])

        total_attitude = modelSalary.attitude(perilaku, disiplin, kejujuran, tanggung_jawab)
        at_1 = Attitude(perilaku, disiplin, kejujuran, tanggung_jawab, total_attitude)

        # ACHIEVEMENT
        pencapaian = float(request.form['pencapaian'])
        pengalaman_bekerja = float(request.form['pengalaman_bekerja'])
        gaji = float(request.form['gaji'])
        level_pekerjaan = float(request.form['level_pekerjaan'])

        position_status = 'Mahasiswa'
        if level_pekerjaan == 1:
            position_status = 'Mahasiswa'
        elif  level_pekerjaan == 2:
            position_status = 'Junior Level'
        elif  level_pekerjaan == 3:
            position_status = 'Middle Level'
        elif  level_pekerjaan == 4:
            position_status = 'Senior Level'
        elif  level_pekerjaan == 5:
            position_status = 'Managerial'

        total_achievement = modelSalary.achievement(pencapaian, pengalaman_bekerja, gaji, level_pekerjaan)
        a_1 = Achievement(int(pencapaian), pengalaman_bekerja, int(gaji), position_status, total_achievement)

        final_salary = modelSalary.fuzzyStageTwo(total_personal_information, total_skills, total_attitude, total_achievement)

        final_result = True

        return render_template('result.html', pi = pi_1, ac = a_1, at = at_1, sk = s_1, final_salary = final_salary)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)