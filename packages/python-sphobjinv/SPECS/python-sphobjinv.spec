%global pypi_name sphobjinv

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        2%{?dist}
Summary:        Sphinx objects.inv inspection/manipulation tool

License:        MIT
URL:            https://github.com/bskinn/sphobjinv
Source0:        %{pypi_source}
BuildArch:      noarch

%description
The syntax required for a functional Sphinx cross-reference is highly
non-obvious in many cases. Sometimes Sphinx can guess correctly what
you mean, but it’s pretty hit-or-miss. The best approach is to provide
Sphinx with a completely specified cross-reference, and that’s where
sphobjinv comes in.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
The syntax required for a functional Sphinx cross-reference is highly
non-obvious in many cases. Sometimes Sphinx can guess correctly what
you mean, but it’s pretty hit-or-miss. The best approach is to provide
Sphinx with a completely specified cross-reference, and that’s where
sphobjinv comes in.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
sed -i "s|\r||g" README.rst


%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{_bindir}/sphobjinv
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.9

* Mon Mar 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.1-1
- Initial package for Fedora
