using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(fileName = "TextMessage", menuName = "ScriptableObjects/TextMessageObject", order = 1)]
public class TextMessageScriptableObject : ScriptableObject
{
    public string sender;
    public string content;
    public Sprite profilPicture;
}
