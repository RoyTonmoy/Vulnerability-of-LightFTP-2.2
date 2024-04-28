# INSE6140-Project - Exploring and patching directory traversal vulnerability of LightFTP server

# LightFTP Directory Traversal Patch

This repository contains our work on identifying and patching a directory traversal vulnerability in the LightFTP server, specifically targeted at CVE-2023-24042. Our project was completed as part of the coursework for INSE6140, Winter 2024.

## About LightFTP

LightFTP is an open-source FTP server designed for:
- Personal file sharing
- Embedded system development
- Education and learning purposes

The server is written in C and supports both x86-32 and x64 architectures. The version affected by the vulnerability is 2.2.

## Vulnerability Overview

The directory traversal vulnerability in LightFTP allows an attacker to access files and directories stored on the server that are outside the intended permissive directories. This vulnerability stems from improper handling of file paths in FTP commands.

## Patching Methodology

Our approach to patching this vulnerability involved several steps:
1. Analyzing the source code to understand the flow and implementation.
2. Identifying the specific areas where the vulnerability exists.
3. Exploiting the vulnerability to confirm its existence and test its implications.
4. Writing a patch that addresses the vulnerability.
5. Retesting the same exploit methods to ensure the vulnerability was effectively mitigated.

## Patch Description

We addressed the vulnerability using both detection and prevention techniques, which involve:
- Adding a new variable to the context structure to handle path corrections.
- Modifying the `ftpUSER` and `ftpPASS` functions to properly handle incoming path requests and ensure they are contained within the root directory.



### Prerequisites

Ensure you have a C compiler and standard build tools installed.


## Acknowledgements

- Md Ariful Haque
- Md. Khiruzzaman
- Tonmoy Roy

Special thanks to our course instructor Dr. Makan Pourzandi and peers at INSE6140 for their guidance and support throughout this project.
