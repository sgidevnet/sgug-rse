%global bootstrap 0

Name:           python-pymongo
Version:        3.8.0
Release:        2%{?dist}

# All code is ASL 2.0 except bson/time64*.{c,h} which is MIT
License:        ASL 2.0 and MIT
Summary:        Python driver for MongoDB
URL:            http://api.mongodb.org/python
Source0:        https://github.com/mongodb/mongo-python-driver/archive/%{version}/pymongo-%{version}.tar.gz
# This patch removes the bundled ssl.match_hostname library as it was vulnerable to CVE-2013-7440
# and CVE-2013-2099, and wasn't needed anyway since Fedora >= 22 has the needed module in the Python
# standard library. It also adjusts imports so that they exclusively use the code from Python.
Patch01:        0001-Use-ssl.match_hostname-from-the-Python-stdlib.patch

BuildRequires:  gcc
%if 0%{!?bootstrap:1}
BuildRequires:  python3-sphinx
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
The Python driver for MongoDB.


%package doc
BuildArch: noarch
Summary:   Documentation for python-pymongo

%description doc
Documentation for python-pymongo.


%package -n python3-bson
Summary:        Python bson library
%{?python_provide:%python_provide python3-bson}

%description -n python3-bson
BSON is a binary-encoded serialization of JSON-like documents. BSON is designed
to be lightweight, traversable, and efficient. BSON, like JSON, supports the
embedding of objects and arrays within other objects and arrays.  This package
contains the python3 version of this module.


%package -n python3-pymongo
Summary:        Python driver for MongoDB
Requires:       python3-bson%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-pymongo}

%description -n python3-pymongo
The Python driver for MongoDB.  This package contains the python3 version of
this module.


%package -n python3-pymongo-gridfs
Summary:        Python GridFS driver for MongoDB
Requires:       python3-pymongo%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-pymongo-gridfs}

%description -n python3-pymongo-gridfs
GridFS is a storage specification for large objects in MongoDB.  This package
contains the python3 version of this module.


%prep
%setup -q -n mongo-python-driver-%{version}
%patch01 -p1 -b .ssl

# Remove the bundled ssl.match_hostname library as it was vulnerable to CVE-2013-7440
# and CVE-2013-2099, and isn't needed anyway since Fedora >= 22 has the needed module in the Python
# standard library.
rm pymongo/ssl_match_hostname.py


%build
%py3_build

%if 0%{!?bootstrap:1}
pushd doc
make %{?_smp_mflags} html
popd
%endif


%install
%py3_install
# Fix permissions
chmod 755 %{buildroot}%{python3_sitearch}/bson/*.so
chmod 755 %{buildroot}%{python3_sitearch}/pymongo/*.so


%files doc
%license LICENSE
%if 0%{!?bootstrap:1}
%doc doc/_build/html/*
%endif


%files -n python3-bson
%license LICENSE
%doc README.rst
%{python3_sitearch}/bson


%files -n python3-pymongo
%license LICENSE
%doc README.rst
%{python3_sitearch}/pymongo
%{python3_sitearch}/pymongo-%{version}-*.egg-info


%files -n python3-pymongo-gridfs
%license LICENSE
%doc README.rst
%{python3_sitearch}/gridfs


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0 (#1686670).
- http://api.mongodb.com/python/3.8.0/changelog.html

* Tue Mar 26 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.7.2-2
- Drop build dependency on mongodb-server, since it is no longer shipped in Fedora.
- As a result of the above, we no longer run the tests.

* Thu Feb 28 2019 Yatin Karel <ykarel@redhat.com> - 3.7.2-1
- Update to 3.7.2
- http://api.mongodb.com/python/3.7.2/changelog.html

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Miro Hrončok <mhroncok@redhat.com> - 3.7.1-3
- Subpackages python2-bson, python2-pymongo, python2-pymongo-gridfs have been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Dec 10 2018 Honza Horak <hhorak@redhat.com> - 3.7.1-3
- Add bootstrap macro and python2 condition

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.7.1-2
- Rebuild with fixed binutils

* Mon Jul 30 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1 (#1601651).
- http://api.mongodb.com/python/3.7.1/changelog.html

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.6.1-2
- Rebuilt for Python 3.7

* Sat Mar 10 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1 (#1550757).
- http://api.mongodb.com/python/3.6.1/changelog.html

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.6.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Feb 19 2018 Marek Skalický <mskalick@redhat.com> - 3.6.0-1
- Rebase to latest release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
