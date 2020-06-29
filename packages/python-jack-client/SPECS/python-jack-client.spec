%global srcname0 JACK-Client
%global srcname1 jackclient-python
%global srcname2 JACK_Client

Name:          python-jack-client
Version:       0.5.2
Release:       2%{?dist}
Summary:       JACK Audio Connection Kit (JACK) Client for Python
BuildArch:     noarch

License:       MIT

URL:           http://jackclient-python.rtfd.org
Source0:       https://github.com/spatialaudio/jackclient-python/archive/%{version}/%{srcname0}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-cffi
%{?python_provide:%python_provide %{name}}
Requires:      python3-cffi
Requires:      jack-audio-connection-kit
Suggests:      python3-numpy

%description
Python module that provides bindings for the JACK library.
The module is able to create audio input and output ports,
also provides the functionality to manage MIDI ports.

This package installs the library for Python.

%prep
%autosetup -n %{srcname1}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%license LICENSE
%doc README.rst
%doc NEWS.rst
%doc CONTRIBUTING.rst
%{python3_sitelib}/%{srcname2}-*.egg-info/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/_jack.py
%{python3_sitelib}/jack.py

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-2
- Rebuilt for Python 3.9

* Mon Feb 17 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 0.5.2-1
- Initial release for Fedora
