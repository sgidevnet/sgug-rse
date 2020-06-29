%global pname periodictable

%bcond_without check

%global _description %{expand:
This package provides a periodic table of the elements
with support for mass, density and xray/neutron
scattering information.

Masses, densities and natural abundances come from
the NIST Physics Laboratory, but do not represent a
critical evaluation by NIST scientists.

Neutron scattering calculations use values collected
by the Atomic Institute of the Austrian Universities.
These values do corresponding to those from other packages,
though there are some differences depending to the tables used.
Bound coherent neutron scattering for gold in particular is
significantly different from older value: 7.63(6) as 
easured in 1974 compared to 7.90(7) as measured in 1990.

X-ray scattering calculations use a combination of empirical
and theoretical values from the LBL Center for X-ray Optics.
These values differ from those given in other sources such as
the International Tables for Crystallography, Volume C, and so
may give different results from other packages.}

Name:           python-%{pname}
Version:        1.5.2
Release:        4%{?dist}
Summary:        Extensible periodic table of the elements

# periodictable/cromermann.py: BSD 3-clause "New" or "Revised" License
# https://github.com/pkienzle/periodictable/issues/30
License:        Public Domain and BSD
URL:            http://www.reflectometry.org/danse/elements.html
Source0:        https://github.com/pkienzle/%{pname}/archive/v%{version}/%{pname}-%{version}.tar.gz
BuildArch:      noarch

%description
%{_description}.

%package -n python%{python3_pkgversion}-%{pname}
Summary: Extensible periodic table of the elements

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pyparsing
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pname}}

%description -n python%{python3_pkgversion}-%{pname}
%{_description}.


%prep
%autosetup -n %{pname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
pushd test
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v
%endif

%files -n python%{python3_pkgversion}-%{pname}
%{python3_sitelib}/*egg-info/
%{python3_sitelib}/%{pname}/

%changelog
* Wed Jun 24 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.5.2-4
- Switch to pytest

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-3
- Rebuilt for Python 3.9

* Tue Mar 03 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.5.2-2
- Switch to pytest

* Fri Feb 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.5.2-1
- First release
