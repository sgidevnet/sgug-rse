# what it's called on pypi
%global srcname h11
# what it's imported as
%global libname h11
# name of egg info directory
%global eggname h11
# package name fragment
%global pkgname h11

%global _description \
This is a little HTTP/1.1 library written from scratch in Python, heavily\
inspired by hyper-h2.  It is a "bring-your-own-I/O" library; h11 contains no IO\
code whatsoever.  This means you can hook h11 up to your favorite network API,\
and that could be anything you want: synchronous, threaded, asynchronous, or\
your own implementation of RFC 6214 -- h11 will not judge you.  This also means\
that h11 is not immediately useful out of the box: it is a toolkit for building\
programs that speak HTTP, not something that could directly replace requests or\
twisted.web or whatever.  But h11 makes it much easier to implement something\
like requests or twisted.web.

%bcond_without tests


Name:           python-%{pkgname}
Version:        0.9.0
Release:        6%{?dist}
Summary:        A pure-Python, bring-your-own-I/O implementation of HTTP/1.1
License:        MIT
URL:            https://github.com/python-hyper/h11
Source0:        %pypi_source
BuildArch:      noarch


%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
py.test-%{python3_version} --verbose
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Carl George <carl@george.computer> - 0.9.0-1
- Latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 12 2018 Carl George <carl@george.computer> - 0.8.1-1
- Initial package
