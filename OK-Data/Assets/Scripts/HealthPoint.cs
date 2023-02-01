using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;

public class HealthPoint : MonoBehaviour
{
    public string nameValue;
    public int HealtPointLeft = 20;
    private TMP_Text displayPoints; 
    private int rankHealthElement;

    void Start()
    {  
        //target text field to display value score
        Transform objectText = transform.GetChild(1).GetChild(1);
        rankHealthElement = transform.GetSiblingIndex();
        
        //display value score
        displayPoints = objectText.GetComponent<TMP_Text>();
        HealthBar.healthValues[rankHealthElement] = HealtPointLeft;
    }

    void Update()
    {
        HealthBar.healthValues[rankHealthElement] = HealtPointLeft;
        displayPoints.SetText(HealthBar.healthValues[rankHealthElement].ToString());
    }
}

