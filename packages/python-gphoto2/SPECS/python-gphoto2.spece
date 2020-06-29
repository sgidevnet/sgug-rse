%global pypi_name gphoto2

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        6%{?dist}
Summary:        A Python interface to libgphoto2

License:        GPLv3+
URL:            https://github.com/jim-easterbrook/python-gphoto2
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  libgphoto2-devel
BuildRequires:  pkgconfig

%description
python-gphoto2 is a comprehensive Python interface (or binding) to libgphoto2.
It is built using SWIG to automatically generate the interface code. This 
ives direct access to nearly all the libgphoto2 functions, but sometimes in
a rather un-Pythonic manner.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
python-gphoto2 is a comprehensive Python interface (or binding) to libgphoto2.
It is built using SWIG to automatically generate the interface code. This
gives direct access to nearly all the libgphoto2 functions, but sometimes in
a rather un-Pythonic manner.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove shebang
sed -e '1d' -i examples/*.py
# Examples don't need to be executable
chmod -x examples/*.py

%build
%py3_build

%install
%py3_install
# Data files are goining to the wrong location
rm -rf %{buildroot}%{_datadir}/%{name}

%files -n python3-%{pypi_name}
%doc CHANGELOG.txt README.rst examples
%license LICENSE.txt
%{python3_sitearch}/*.egg-info
%{python3_sitearch}/%{pypi_name}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.0-1
- Initial package for Fedora
