%global pypi_name xlsxwriter
%global src_name XlsxWriter

Name:		python-%{pypi_name}
Version:	1.2.9
Release:	1%{?dist}
Summary:	Python module for writing files in the Excel 2007+ XLSX file format
License:	BSD
URL:		https://pypi.python.org/pypi/XlsxWriter
Source0:	https://files.pythonhosted.org/packages/source/X/%{src_name}/%{src_name}-%{version}.tar.gz

BuildArch:	noarch

%global common_desc\
XlsxWriter is a Python module for writing files in the Excel 2007+\
XLSX file format.\
\
XlsxWriter can be used to write text, numbers, formulas and hyperlinks\
to multiple worksheets and it supports features such as formatting and\
many more, including:\
\
	100% compatible Excel XLSX files.\
	Full formatting.\
	Merged cells.\
	Defined names.\
	Charts.\
	Autofilters.\
	Data validation and drop down lists.\
	Conditional formatting.\
	Worksheet PNG/JPEG images.\
	Rich multi-format strings.\
	Cell comments.\
	Integration with Pandas.\
	Textboxes.\
	Memory optimization mode for writing large files.\
\
It supports Python 2.7, 3.4+, Jython and PyPy and uses standard libraries only.

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:		Python 3 modules for writing files in the Excel 2007+ XLSX file format
BuildRequires:	python3-setuptools
BuildRequires:	python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{common_desc}

%prep
%setup -q -n %{src_name}-%{version}
# Remove bundled egg-info
rm -rf %{src_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{src_name}-%{version}-py?.?.egg-info
%{_bindir}/vba_extract.py

%changelog
* Sat May 30 2020 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.2.9-1
- Added support for stacked and percent_stacked Line charts

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.8-2
- Rebuilt for Python 3.9

* Sun Feb 23 2020 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.2.8-1
- Fix for issue where duplicate images with hyperlinks weren’t handled correctly
- Removed ReservedWorksheetName exception which was used with the reserved worksheet name 'History'
- Fix for worksheet objects (charts, images and textboxes) that are inserted with an offset that starts in a hidden cell
- Fix to allow handling of NoneType in add_write_handler()

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.2.7-1
- New version 1.2.7
- Fix for duplicate images being copied to an XlsxWriter file
- Added documentation on Number Format Categories and Number Formats in different locales
- Added note to protect() about how it is possible to encrypt an XlsxWriter file using msoffice-crypt

* Tue Nov 19 2019 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.2.6-1
- New version 1.2.6
- Added option to remove style from worksheet tables - 1.2.6
- Added option to add hyperlinks to textboxes - 1.2.5
- Added option to link textbox text from a cell - 1.2.4
- Added option to rotate text in a textbox - 1.2.4
- Increased allowable worksheet url length from 255 to 2079 characters - 1.2.3
- Fixed several issues with hyperlinks in worksheet images - 1.2.3
- Fixed Python 3.8.0 warnings - 1.2.2

* Mon Sep 16 2019 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.2.1-1
- New version 1.2.1
- Added the add_write_handler() method to allow user defined types to be handled by the write() method
- Add support for East Asian vertical fonts in charts

* Sat Aug 31 2019 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.2.0-1
- New version 1.2.0
- Refactored exception handling around the workbook file close() method
- Added the option to allow chart fonts to be rotated to 270 degrees

* Thu Aug 22 2019 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.1.9-1
- New version 1.1.9

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.1.8-1
- New version 1.1.8

* Sun Apr 21 2019 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.1.7-1
- New version 1.1.7

* Mon Apr 08 2019 Rajeesh KV <rajeeshknambiar@fedoraproject.org> 1.1.6-1
- Release 1.1.6, fix issues with  images that started in hidden rows/columns
- and mime-type reported by system file(1)

* Mon Mar 11 2019 Rajeesh KV <rajeeshknambiar@fedoraproject.org> 1.1.5-1
- Release 1.1.5, initial packaging for Fedora
