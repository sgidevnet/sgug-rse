%global modname kadmin
%global commit          94e50ed0a788d9ff9e4b47a35a65ca22c69b703a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20181207

Name:               python-kadmin
Version:            0.1.2
Release:            9.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:            Python module for kerberos admin (kadm5)

License:            MIT
URL:                https://github.com/rjancewicz/python-%{modname}
Source0:            %{url}/archive/%{commit}/python-%{modname}-%{shortcommit}.tar.gz
Patch0:             https://patch-diff.githubusercontent.com/raw/rjancewicz/python-kadmin/pull/59.patch#/0001-build-one-package-with-two-extensions.patch
Patch1:             12de82aa48a7faeb5bfc618a226f2cc388e2eb4d.patch
%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      krb5-devel
BuildRequires:      bison
BuildRequires:      gcc

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
%autosetup -p1 -n python-%{modname}-%{commit}

%build
export CFLAGS="$CFLAGS -fcommon"
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{modname}
%doc README.md
%license LICENSE.txt
%{python3_sitearch}/%{modname}*.so
%{python3_sitearch}/python_%{modname}*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-9.20181207git94e50ed
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.1.2-8.20181207git94e50ed
- Patch for bad call flags.

* Fri Mar 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.1.2-7.20181207git94e50ed
- krb5 rebuild.

* Wed Jan 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.1.2-6.20181207git94e50ed
- Build with -fcommon for gcc10.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-5.20181207git94e50ed
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1.2-3.20181207git94e50ed
- Rebuild for krb5.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2.20181207git94e50ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.1.2-1.20181207git94e50ed
- Corrected URL/Source/Patch, from review.

* Fri Dec 07 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.1.2-1.20181207
- Initial package.
