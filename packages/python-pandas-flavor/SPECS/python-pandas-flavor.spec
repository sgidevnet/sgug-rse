%global pypi_name pandas_flavor

%global _description %{expand:
The easy way to write your own flavor of Pandas

Pandas 0.23 added a (simple) API for registering accessors with Pandas objects.

Pandas-flavor extends Pandas extension API by:

- adding support for registering methods as well.
- making each of these functions backwards compatible with older versions of
  Pandas.
}

Name:           python-pandas-flavor
Version:        0.1.2
Release:        3%{?dist}
Summary:        The easy way to write your own Pandas flavor

License:        MIT
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        %pypi_source
# Fetch the license from the github repository
Source1:        https://raw.githubusercontent.com/Zsailer/pandas_flavor/master/LICENSE

BuildArch:      noarch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
cp -pv %{SOURCE1} .

# rm -rf %%{pypi_name}.egg-info

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.2-1
- Update as per review comments
- https://bugzilla.redhat.com/show_bug.cgi?id=1770496
- Comment out egg info removal
- use -p in cp to preserve time stamp

* Sat Nov 09 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.2-1
- Initial build
