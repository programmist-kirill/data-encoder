using System;
using System.IO;

namespace rename1
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			System.IO.File.Move("D:/Project/Python/script/script_encoder/name.txt", "D:/Project/Python/script/script_encoder/path.exe");
			System.IO.File.Move("D:/Project/Python/script/script_encoder/password.txt", "D:/Project/Python/script/script_encoder/security.exe");
		}
	}
}
