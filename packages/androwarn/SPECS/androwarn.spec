Name:           androwarn
Version:        1.6.1
Release:        4%{?dist}
Summary:        Static code analyzer for malicious Android applications

# androwarn is LGPL, Twitter Bootstrap is ASL 2.0 and jQuery MIT
License:        LGPLv3+ and ASL 2.0 and MIT
URL:            https://github.com/maaaaz/androwarn
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Androwarn is a tool whose main aim is to detect and warn the user about
potential malicious behaviors developed by an Android application.

The detection is performed with the static analysis of the application's
Dalvik bytecode, represented as Smali, with the androguard library.

This analysis leads to the generation of a report, according to a technical
detail level chosen from the user.

%prep
%autosetup
rm -rf androwarn/{_SampleApplication,_SampleReports}
chmod -x androwarn/{README.md,COPYING,COPYING.LESSER}
# Handle requirements with dep generator
rm -rf androwarn/requirements.txt
sed -i -e "s/'argparse',//g" setup.py
sed -i -e '/^#!\//, 1d' androwarn/{__init__.py,androwarn.py,warn/*/*.py,warn/*/*/*.py}
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%files
%doc androwarn/README.md
%license androwarn/COPYING androwarn/COPYING.LESSER
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-4
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.1-3
- Enable dep generator and fix requirements handling

* Tue Jan 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.1-2
- Disable dep generator
- Add missing BR (rhbz#1790091)

* Sat Dec 14 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.6.1-1
- Initial package for Fedora
