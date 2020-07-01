%global pypi_name mulpyplexer

Name:           python-%{pypi_name}
Version:        0.08
Release:        2%{?dist}
Summary:        Module that multiplexes interactions with lists of Python objects

License:        BSD
URL:            https://github.com/zardus/mulpyplexer
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/zardus/mulpyplexer/master/LICENSE
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Mulpyplexer is a piece of code that can multiplex interactions with lists of
python objects.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Mulpyplexer is a piece of code that can multiplex interactions with lists of
python objects.

%prep
%autosetup -n %{pypi_name}-%{version}
cp -a %{SOURCE1} LICENSE

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.08-2
- Rebuilt for Python 3.9

* Sat Mar 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.08-2
- Add license file (rhbz#1808506) 

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.08-1
- Initial package for Fedora
