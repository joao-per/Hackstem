using UnityEngine;
using UnityEngine.Networking;
using TMPro;
using System.Collections;

public class RegisterManager : MonoBehaviour
{
	// Referências da UI
	public TMP_InputField nameField;
	public TMP_InputField emailField;
	public TMP_InputField passwordField;
	public GameObject registerPanel;
	public GameObject popup;
	public TMP_Text popupText;

	private string apiUrl = "http://yourApiUrlHere.com/user";

	public void Register()
	{
		string name = nameField.text;
		string email = emailField.text;
		string password = passwordField.text;

		StartCoroutine(RegisterCoroutine(name, email, password));
	}

	private IEnumerator RegisterCoroutine(string name, string email, string password)
	{
		WWWForm form = new WWWForm();
		form.AddField("name", name);
		form.AddField("email", email);
		form.AddField("password", password);

		using (UnityWebRequest www = UnityWebRequest.Post(apiUrl, form))
		{
			yield return www.SendWebRequest();

			if (www.result != UnityWebRequest.Result.Success)
			{
				Debug.Log(www.error);
				ShowPopup("Dados de Login incorretos");
			}
			else
			{
				Debug.Log("Conta criada com sucesso!");
				ShowPopup("Conta registrada com sucesso!");
				registerPanel.SetActive(false);
			}
		}
	}

	private void ShowPopup(string message)
	{
		popupText.text = message;
		popup.SetActive(true);
		//wait 5 seconds and hide popup
		StartCoroutine(HidePopup());
	}

	private IEnumerator HidePopup()
	{
		yield return new WaitForSeconds(2);
		popup.SetActive(false);
	}
}
