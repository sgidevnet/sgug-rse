%global pypi_name yaswfp

Name:           python-%{pypi_name}
Version:        0.9.3
Release:        4%{?dist}
Summary:        Yet Another SWF Parser in Python

License:        GPLv3+
URL:            http://github.com/facundobatista/yaswfp
Source0:        https://files.pythonhosted.org/packages/source/y/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Yet Another SWF Parser that can help you to identify SWF objects.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Yet Another SWF Parser that can help you to identify SWF objects.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING
%{_bindir}/swfparser
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-2
- Better use of wildcards (rhbz#1787224)

* Wed Jan 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-1
- Initial package for Fedora
