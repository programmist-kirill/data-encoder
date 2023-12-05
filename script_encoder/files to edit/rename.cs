using System;
using System.IO;

namespace rename
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			System.IO.File.Move("D:/project/python/script/script_encoder/configuration.txt", "D:/project/python/script/script_encoder/script.config");
		}
	}
}
