using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class clockDisplay : MonoBehaviour
{
    public TMP_Text clockText;
    //set time to be display
    static int hour = 12;
    static int minute = 52;
    
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //display time in a string format like 13:52
        clockText.text = string.Format("{0:0}:{1:00}",(float)hour,(float)minute);    
       // clockText.text = string.Format("{0:0}:{1:00}",System.DateTime.Now.Hour,System.DateTime.Now.Minute);
    }
}
