"""Ajoute la permission micro et la déclaration du service vocal Android."""
import pathlib
p = pathlib.Path("android/app/src/main/AndroidManifest.xml")
t = p.read_text(encoding="utf-8")
if "RECORD_AUDIO" not in t:
    t = t.replace("</manifest>", '    <uses-permission android:name="android.permission.RECORD_AUDIO" />\n</manifest>')
if "android.speech.RecognitionService" not in t:
    t = t.replace("</manifest>", '    <queries>\n        <intent>\n            <action android:name="android.speech.RecognitionService" />\n        </intent>\n    </queries>\n</manifest>')
p.write_text(t, encoding="utf-8")
print("AndroidManifest.xml mis à jour")
