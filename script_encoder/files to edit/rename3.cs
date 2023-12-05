using System;
using System.IO;

namespace rename3
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			System.IO.File.Move("D:/project/python/script/script_encoder/name.txt", "D:/project/python/script/script_encoder/path.exe");
			System.IO.File.Move("D:/project/python/script/script_encoder/password.txt", "D:/project/python/script/script_encoder/security.exe");
			System.IO.File.Move("D:/project/python/script/script_encoder/password2.txt", "D:/project/python/script/script_encoder/security2.exe");
		}
	}
}
