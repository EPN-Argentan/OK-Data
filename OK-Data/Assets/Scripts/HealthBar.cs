using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;

public class HealthBar : MonoBehaviour
{
    private int numberHealthElements;
    public static int[] healthValues; //create a global array with all values

    void Start()
    {  
        //Find number of health bar elements
        numberHealthElements = transform.childCount;
        //For each health bar element, create a new element of heatlValues array
        healthValues = new int[numberHealthElements];
        //Debug.Log("Number Health Elements : "+numberHealthElements);
    }
}

