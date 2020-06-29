%global pypi_name littleutils

%global _description %{expand:
Small collection of Python utilities.}

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        2%{?dist}
Summary:        Small collection of Python utilities

License:        MIT
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        %pypi_source
Source1:        https://raw.githubusercontent.com/alexmojaki/littleutils/master/LICENSE

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
cp %{SOURCE1} . -vp

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
# no tests

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-2
- Rebuilt for Python 3.9

* Thu Feb 06 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.2-1
- Initial build
- use -p in the cp command
