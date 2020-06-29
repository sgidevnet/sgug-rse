%global pypi_name python-rtmidi
%global srcname rtmidi

Name:           python-%{srcname}
Version:        1.3.1
Release:        3%{?dist}
Summary:        Python binding for the RtMidi C++ library

License:        MIT
URL:            https://chrisarndt.de/projects/python-rtmidi/
Source0:        %{pypi_source %{pypi_name}}

BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  jack-audio-connection-kit-devel

%description
python-rtmidi is a Python binding for RtMidi implemented using Cython and
provides a thin wrapper around the RtMidi C++ interface. The API is basically
the same as the C++ one but with the naming scheme of classes, methods and
parameters adapted to the Python PEP-8 conventions and requirements of the
Python package naming structure.

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
#BuildRequires:  python3-tox
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
python-rtmidi is a Python binding for RtMidi implemented using Cython and
provides a thin wrapper around the RtMidi C++ interface. The API is basically
the same as the C++ one but with the naming scheme of classes, methods and
parameters adapted to the Python PEP-8 conventions and requirements of the
Python package naming structure.

%package -n python-%{srcname}-doc
Summary:        %{srcname} documentation

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-websupport

%description -n python-%{srcname}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH={PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# The tox tests are excessive (Py2), pyteet is not working out of-the-box
# and they requires a running JACK server
#%check
#%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE.txt docs/license.rst
%doc README.rst
%{python3_sitearch}/rtmidi/
%{python3_sitearch}/python_rtmidi-%{version}-py*.egg-info

%files -n python-%{srcname}-doc
%doc html
%license LICENSE.txt docs/license.rst

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.3.1-1
- Initial package
