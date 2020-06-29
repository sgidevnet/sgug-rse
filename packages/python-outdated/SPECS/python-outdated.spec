# Require net access
# Test in mock:
# mock -r fedora-rawhide-x86_64 rebuild ./python-outdated-0.2.0-1.fc31.src.rpm --with=tests --enable-network
%bcond_with tests

%global pypi_name outdated

%global _description %{expand:
Check if a version of a PyPI package is outdated.}

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Check if a version of a PyPI package is outdated

License:        MIT
URL:            https://pypi.org/pypi/%{pypi_name}
Source0:        %pypi_source
# No release on github so I just use these as sources
Source1:        https://raw.githubusercontent.com/alexmojaki/%{pypi_name}/master/LICENSE
Source2:        https://raw.githubusercontent.com/alexmojaki/%{pypi_name}/master/README.md
Source3:        https://raw.githubusercontent.com/alexmojaki/%{pypi_name}/master/tests.py

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
%if %{with tests}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist littleutils}
%endif

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# Copy over sources
cp %SOURCE1 . -vp
cp %SOURCE2 . -vp
cp %SOURCE3 . -vp

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -m unittest
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-2
- Rebuilt for Python 3.9

* Thu Feb 06 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.0-1
- Initial build
- Enable test
