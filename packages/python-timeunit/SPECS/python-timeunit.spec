# Created by pyp2rpm-3.3.2
%global pypi_name timeunit

%global desc \
Based on java.util.concurrent.TimeUnit and timeunit in npm \
TimeUnit is a port of the public domain TimeUnit Java class by Doug Lea \
This class is the basis for java.util.concurrent.TimeUnit from JavaSE. \
 \
A timeunit represents time durations at a given unit of granularity and \
provides utility methods to convert across units, and to perform delay \
operations in these units. A timeunit does not maintain time information, \
but only helps organize and use time representations that may be maintained \
separately across various contexts. \
 \
A timeunit is mainly used to inform time-based methods how a given timing \
parameter should be interpreted.


Name:           python-%{pypi_name}
Version:        1.1.0
Release:        3%{?dist}
Summary:        Python module providing utility methods to convert across time units

License:        MIT
URL:            https://github.com/Ralph-Wang/timeunit-python
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
#README.md contains the LICENSE text upstream, split this up
awk '/^## License/ {++count; file="LICENSE.md"; print file} file {print line > file} {line=$0}' README.md
sed -i '/## License[^.]*$/,+30 g' README.md

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE.md
%{python3_sitelib}/timeunit*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 28 2019 David McCheyne <davidmccheyne@gmail.com> - 1.1.0-1
- Initial package.
