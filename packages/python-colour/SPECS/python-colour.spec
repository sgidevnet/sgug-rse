%global pypi_name colour

Name:           python-%{pypi_name}
Version:        0.1.5
Release:        6%{?dist}
Summary:        Python module to convert and manipulate color representations

License:        BSD
URL:            https://github.com/vaab/colour
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Converts and manipulates common color representation (RGB, HSL, web, etc.)

- Damn simple and pythonic way to manipulate color representation
- Full conversion between RGB, HSL, 6-digit hex, 3-digit hex, human color
- One object (Color) or bunch of single purpose function (rgb2hex, hsl2rgb,
  etc.) web format that use the smallest representation between 6-digit 
  (e.g. #fa3b2c), 3-digit (e.g. #fbb), fully spelled color (e.g. white),
  following W3C color naming for compatible CSS or HTML color specifications.
- smooth intuitive color scale generation choosing N color gradients.
- can pick colors for you to identify objects of your application.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-d2to1
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Converts and manipulates common color representation (RGB, HSL, web, etc.)

- Damn simple and pythonic way to manipulate color representation
- Full conversion between RGB, HSL, 6-digit hex, 3-digit hex, human color
- One object (Color) or bunch of single purpose function (rgb2hex, hsl2rgb,
  etc.) web format that use the smallest representation between 6-digit 
  (e.g. #fa3b2c), 3-digit (e.g. #fbb), fully spelled color (e.g. white),
  following W3C color naming for compatible CSS or HTML color specifications.
- smooth intuitive color scale generation choosing N color gradients.
- can pick colors for you to identify objects of your application.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst TODO.rst
%license LICENSE
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.5-1
- Initial package for Fedora
