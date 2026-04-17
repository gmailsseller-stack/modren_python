from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# قاعدة البيانات الكاملة
DATABASE = {
    "4210047": "100768",
    "4210067": "109132",
    "4210187": "103478",
    "4210188": "101578",
    "4210221": "132691",
    "4210257": "110951",
    "4210360": "102717",
    "4210447": "101192",
    "4210448": "100698",
    "4210472": "100118",
    "4210494": "106258",
    "4210546": "101839",
    "4210595": "116718",
    "4220002": "100594",
    "4220008": "101414",
    "4220009": "104595",
    "4220020": "101077",
    "4220032": "105578",
    "4220041": "103632",
    "4220043": "101722",
    "4220044": "103493",
    "4220048": "100936",
    "4220049": "100139",
    "4220052": "100253",
    "4220055": "105855",
    "4220056": "105102",
    "4220057": "140974",
    "4220058": "101277",
    "4220061": "101499",
    "4220066": "104352",
    "4220067": "100192",
    "4220085": "102094",
    "4220086": "102874",
    "4220089": "107993",
    "4220092": "103346",
    "4220099": "101372",
    "4220105": "106922",
    "4220110": "100057",
    "4220119": "104516",
    "4220128": "101253",
    "4220129": "103086",
    "4220134": "104669",
    "4220136": "104811",
    "4220139": "103457",
    "4220160": "102371",
    "4220165": "101854",
    "4220171": "100474",
    "4220172": "100518",
    "4220175": "105239",
    "4220181": "103933",
    "4220185": "104017",
    "4220196": "109819",
    "4220198": "104772",
    "4220200": "101573",
    "4220203": "104511",
    "4220211": "100955",
    "4220213": "101225",
    "4220216": "101356",
    "4220225": "102864",
    "4220230": "105716",
    "4220235": "103563",
    "4220236": "113036",
    "4220238": "105331",
    "4220240": "100074",
    "4220249": "100558",
    "4220255": "101502",
    "4220257": "106454",
    "4220261": "103259",
    "4220267": "103935",
    "4220277": "100073",
    "4220282": "100305",
    "4220286": "100216",
    "4220290": "100759",
    "4220300": "100366",
    "4220301": "102754",
    "4220313": "100975",
    "4220317": "106057",
    "4220319": "108634",
    "4220323": "108132",
    "4220339": "100879",
    "4220343": "101216",
    "4220348": "102092",
    "4220351": "100594",
    "4220361": "101495",
    "4220364": "100172",
    "4220375": "105468",
    "4220380": "101176",
    "4220389": "101835",
    "4220401": "103623",
    "4220407": "102984",
    "4220413": "100795",
    "4220419": "102276",
    "4220420": "100191",
    "4220422": "100258",
    "4220434": "102655",
    "4220448": "100432",
    "4220461": "103669",
    "4220492": "100591",
    "4220498": "103254",
    "4220506": "100698",
    "4220507": "100356",
    "4220509": "100065",
    "4220512": "106078",
    "4220528": "102943",
    "4220529": "101368",
    "4220531": "101511",
    "4220535": "108081",
    "4220542": "102656",
    "4220559": "102425",
    "4230028": "112414",
    "4230037": "100494",
    "4230089": "101076",
    "4230146": "102214",
    "4230227": "100178",
    "4230390": "100171",
    "4230448": "100232",
    "4230526": "102339",
    "4230547": "103179",
    "4230581": "101255",
    "4230584": "100432",
    "4230585": "104266",
    "4230598": "101314",
    "4230735": "100776",
    "4230869": "101352",
    "4230915": "109758",
    "4240470": "100963",
    "4240580": "100501"
}

# قالب HTML
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>البحث عن كلمة المرور - أكاديمية مصر الحديثة</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Tahoma', 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            padding: 40px;
            max-width: 500px;
            width: 100%;
            text-align: center;
        }
        h1 { color: #333; margin-bottom: 10px; font-size: 24px; }
        .subtitle { color: #666; margin-bottom: 30px; font-size: 14px; }
        input {
            width: 100%;
            padding: 15px;
            font-size: 18px;
            border: 2px solid #ddd;
            border-radius: 10px;
            text-align: center;
            margin: 20px 0;
            font-family: monospace;
        }
        input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 10px rgba(102,126,234,0.3);
        }
        button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 10px;
            cursor: pointer;
            width: 100%;
            font-weight: bold;
        }
        button:hover { transform: scale(1.02); }
        .result {
            margin-top: 30px;
            padding: 20px;
            border-radius: 10px;
        }
        .success { background: #d4edda; border: 2px solid #28a745; }
        .error { background: #f8d7da; border: 2px solid #dc3545; }
        .password { font-size: 32px; font-weight: bold; font-family: monospace; color: #28a745; margin: 10px 0; }
        footer { margin-top: 30px; font-size: 12px; color: #999; }
        .stats { margin-top: 15px; font-size: 12px; color: #888; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 البحث عن كلمة المرور</h1>
        <div class="subtitle">أكاديمية مصر الحديثة</div>
        
        <form method="POST">
            <input type="text" name="student_id" placeholder="مثال: 4220240" value="{{ student_id or '' }}" autocomplete="off">
            <button type="submit">🔎 بحث</button>
        </form>
        
        {% if result %}
        <div class="result {{ 'success' if result.found else 'error' }}">
            {% if result.found %}
                <div>✅ تم العثور على النتيجة</div>
                <div style="margin: 10px 0;">🆔 رقم الجلوس: <strong>{{ result.student_id }}</strong></div>
                <div class="password">🔑 {{ result.password }}</div>
            {% else %}
                <div>❌ رقم الجلوس {{ result.student_id }} غير موجود</div>
                <div style="margin-top: 10px; font-size: 12px;">💡 الرجاء التأكد من الرقم</div>
            {% endif %}
        </div>
        {% endif %}
        
        <div class="stats">📊 قاعدة البيانات تحتوي على {{ db_size }} سجل</div>
        <footer>⚡ تحديث مستمر | بحث فوري</footer>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    student_id = None
    result = None
    
    if request.method == 'POST':
        student_id = request.form.get('student_id', '').strip()
        password = DATABASE.get(student_id)
        
        if password:
            result = {'found': True, 'student_id': student_id, 'password': password}
        else:
            result = {'found': False, 'student_id': student_id}
    
    return render_template_string(HTML_TEMPLATE, 
                                   student_id=student_id,
                                   result=result,
                                   db_size=len(DATABASE))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
