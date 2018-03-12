# Android Serial (200 pts)

**CTF :** THC 2018

**URL :** https://scoreboard.thcon.party/challenges

## Challenge description 

**APK file :** https://scoreboard.thcon.party/files/e9720efc020b51201ce3039fbb5a4fe3/THC.apk

A commercial Android application for the THC was developed. Unfortunately, its developement has been stopped. 
The application was never released, but be the first to unlock its premium features by finding a valid key.

**Warning:** The flag is not in the format THC{...}

## Solution 


In first time, we're going to decompile the android application **THC.apk** (The lazy way is to use an online APK decompiler :
http://www.javadecompilers.com/apk, it permits to decompile APK to Java). But we could to use too, **JADX** (Command line and GUI tools for produce Java source code from Android Dex and Apk files), thanks to the following command line 

```
jdx -d Serial_Android THC.apk
```

In all producted files, we are only interrested by MainActivity.java (where the serial number is checked) :

``` Java
package com.thc.bestpig.serial;

import android.annotation.TargetApi;
import android.content.DialogInterface;
import android.content.DialogInterface.OnClickListener;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AlertDialog.Builder;
import android.support.v7.app.AppCompatActivity;
import android.text.InputFilter;
import android.text.InputFilter.AllCaps;
import android.text.InputFilter.LengthFilter;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import com.thc.bestpig.test.R;

public class MainActivity extends AppCompatActivity {

    class C02201 implements OnClickListener {
        C02201() {
        }

        public void onClick(DialogInterface dialog, int which) {
            MainActivity.this.startActivity(new Intent(MainActivity.this.getApplicationContext(), PremiumActivity.class));
        }
    }

    class C02212 implements OnClickListener {
        C02212() {
        }

        public void onClick(DialogInterface dialog, int which) {
        }
    }

    protected boolean validateSerial(String serial) {
        if (serial.length() == 19 && serial.charAt(4) == '-' && serial.charAt(9) == '-' && serial.charAt(14) == '-' && serial.charAt(5) == serial.charAt(6) + 1 && serial.charAt(5) == serial.charAt(18) && serial.charAt(1) == (serial.charAt(18) % 4) * 22 && ((serial.charAt(3) * serial.charAt(15)) / serial.charAt(17)) - 1 == serial.charAt(10) && serial.charAt(10) == serial.charAt(1) && serial.charAt(13) == serial.charAt(10) + 5 && serial.charAt(10) == serial.charAt(5) - 9 && (serial.charAt(0) % serial.charAt(7)) * serial.charAt(11) == 1440 && (serial.charAt(2) - serial.charAt(8)) + serial.charAt(12) == serial.charAt(10) - 9 && (serial.charAt(3) + serial.charAt(12)) / 2 == serial.charAt(16) && (serial.charAt(0) - serial.charAt(2)) + serial.charAt(3) == serial.charAt(12) + 15 && serial.charAt(3) == serial.charAt(13) && serial.charAt(16) == serial.charAt(0) && serial.charAt(7) + 1 == serial.charAt(2) && serial.charAt(15) + 1 == serial.charAt(11) && serial.charAt(11) + 3 == serial.charAt(17) && serial.charAt(7) + 20 == serial.charAt(6)) {
            return true;
        }
        return false;
    }

    protected boolean checkPassword(String serial) {
        if (validateSerial(serial)) {
            new Builder(this).setTitle((CharSequence) "Well done ;)").setMessage((CharSequence) "You can now validate this challenge.\n\nThe flag is the serial").setCancelable(false).setNeutralButton((CharSequence) "Ok", new C02201()).show();
            return true;
        }
        new Builder(this).setTitle((CharSequence) "Premium activation failed").setMessage((CharSequence) "Please don't try random serial, buy a legit premium license to support developers.").setCancelable(false).setNeutralButton((CharSequence) "Ok", new C02212()).show();
        return false;
    }

    @TargetApi(21)
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView((int) R.layout.activity_main);
        getSupportActionBar().setDisplayShowHomeEnabled(true);
        getSupportActionBar().setLogo((int) R.mipmap.ic_launcher);
        getSupportActionBar().setDisplayUseLogoEnabled(true);
        final EditText editText = (EditText) findViewById(R.id.serialInput);
        editText.setFilters(new InputFilter[]{new AllCaps(), new LengthFilter(19)});
        ((Button) findViewById(R.id.buttonActivate)).setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                MainActivity.this.checkPassword(editText.getText().toString());
            }
        });
    }
}
```
The following condition verify the serial number : 
```Java

 if (serial.length() == 19 && serial.charAt(4) == '-' && serial.charAt(9) == '-' && serial.charAt(14) == '-' && serial.charAt(5) == serial.charAt(6) + 1 && serial.charAt(5) == serial.charAt(18) && serial.charAt(1) == (serial.charAt(18) % 4) * 22 && ((serial.charAt(3) * serial.charAt(15)) / serial.charAt(17)) - 1 == serial.charAt(10) && serial.charAt(10) == serial.charAt(1) && serial.charAt(13) == serial.charAt(10) + 5 && serial.charAt(10) == serial.charAt(5) - 9 && (serial.charAt(0) % serial.charAt(7)) * serial.charAt(11) == 1440 && (serial.charAt(2) - serial.charAt(8)) + serial.charAt(12) == serial.charAt(10) - 9 && (serial.charAt(3) + serial.charAt(12)) / 2 == serial.charAt(16) && (serial.charAt(0) - serial.charAt(2)) + serial.charAt(3) == serial.charAt(12) + 15 && serial.charAt(3) == serial.charAt(13) && serial.charAt(16) == serial.charAt(0) && serial.charAt(7) + 1 == serial.charAt(2) && serial.charAt(15) + 1 == serial.charAt(11) && serial.charAt(11) + 3 == serial.charAt(17) && serial.charAt(7) + 20 == serial.charAt(6))
```

Find a string to solve all those conditions without any tools is a bit complicaticated (except for Fiora ;) ), thus we chose to use the famous solver
Z3 in its python version **Z3Py**. We converted all conditions into Z3 conditions : 

### Our dirty python script (with love) 


```python
#Team mhackgyver
#THC 2018

from z3 import *


#Declare the Solver used by Z3 and the Array of Int which representing the serial number
s=Solver()
I=IntSort()
tab=Array('tab',I, I)

#Add constraints to our solver
#serial.charAt(4) == '-' && serial.charAt(9) == '-' && serial.charAt(14) == '-' 
s.add(tab[4] == ord('-'))
s.add(tab[9] == ord('-'))
s.add(tab[14] == ord('-'))
#serial.charAt(5) == serial.charAt(6) + 1 
s.add(tab[5] == tab[6] + 1)
#serial.charAt(5) == serial.charAt(18) 
s.add(tab[5] == tab[18])
#erial.charAt(1) == (serial.charAt(18) % 4) * 22 
s.add(tab[1] == ( tab[18] % 4) * 22 )
#((serial.charAt(3) * serial.charAt(15)) / serial.charAt(17)) - 1 == serial.charAt(10) 
s.add(((tab[3] * tab[15]) / tab[17]) - 1 == tab[10] )
# serial.charAt(10) == serial.charAt(1) 
s.add(tab[10] == tab[1] )
# serial.charAt(13) == serial.charAt(10) + 5 
s.add(tab[13] == tab[10] + 5 )
# serial.charAt(10) == serial.charAt(5) - 9 
s.add(tab[10] == tab[5] - 9)
#(serial.charAt(0) % serial.charAt(7)) * serial.charAt(11) == 1440 
#s.add((mod(first[1],second[3]))* third[2] == 1440 )
s.add((tab[0] % tab[7])* tab[11] == 1440 )
# (serial.charAt(2) - serial.charAt(8)) + serial.charAt(12) == serial.charAt(10) - 9 
s.add( (tab[2] - tab[8]) + tab[12] == tab[10] - 9)
# (serial.charAt(3) + serial.charAt(12)) / 2 == serial.charAt(16) 
s.add((tab[3] + tab[12]) / 2 == tab[16])
# (serial.charAt(0) - serial.charAt(2)) + serial.charAt(3) == serial.charAt(12) + 15
s.add((tab[0] - tab[2]) + tab[3] == tab[12] + 15)
# serial.charAt(3) == serial.charAt(13)
s.add(tab[3] == tab[13])
# serial.charAt(16) == serial.charAt(0) 
s.add(tab[16] == tab[0] )
# serial.charAt(7) + 1 == serial.charAt(2)
s.add(tab[7] + 1 == tab[2])
# serial.charAt(15) + 1 == serial.charAt(11) 
s.add(tab[15] + 1 == tab[11])
# serial.charAt(11) + 3 == serial.charAt(17)
s.add(tab[11] + 3 == tab[17])
#serial.charAt(7) + 20 == serial.charAt(6))
s.add(tab[7] + 20 == tab[6])

# Verify and solve our model 
s.check()
print(s.check())
print(s.model())

#Retrieving the model to exploit results 
m=s.model()
res=''

#Retrieving all solutions from the model and converting from the ASCII Code into ASCII char
for j in range(19):
    res=res+chr(int(str(m.eval(tab[j]))))
	
#Print the serial number (HB7G-KJ6G-BPIG-OHSK)
print(res)
```

## Result 

The flag was **HB7G-KJ6G-BPIG-OHSK**
