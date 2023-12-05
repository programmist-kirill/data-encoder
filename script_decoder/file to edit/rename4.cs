using System;
using System.IO;

namespace rename4
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			System.IO.File.Move("D:/project/python/script/script_encoder/path.exe", "D:/project/python/script/script_encoder/name.txt");
			System.IO.File.Move("D:/project/python/script/script_encoder/security.exe", "D:/project/python/script/script_encoder/password.txt");
			System.IO.File.Move("D:/project/python/script/script_encoder/security2.exe", "D:/project/python/script/script_encoder/password2.txt");
		}
	}
}
