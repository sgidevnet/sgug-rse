Name:           pythonabi
Version:        0
Release:        0
Summary:        ...
License:        MIT
BuildRequires:  python3-devel

%description
...

%install
mkdir -p %{buildroot}%{python3_sitelib}
mkdir -p %{buildroot}/opt%{python3_sitelib}
mkdir -p %{buildroot}%{python3_sitearch}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/opt%{_bindir}

echo "print()" > %{buildroot}%{python3_sitelib}/file.py
echo "print()" > %{buildroot}/opt%{python3_sitelib}/file.py

cp %{python3_sitearch}/../lib-dynload/cmath.*.so %{buildroot}%{python3_sitearch}/file.so

cp %{_bindir}/python%{python3_version} %{buildroot}%{_bindir}/python%{python3_version}
cp %{_bindir}/python%{python3_version} %{buildroot}/opt%{_bindir}/python%{python3_version}


%package -n python-noarch
Summary:        ...
BuildArch: noarch
%description -n python-noarch
...
%files -n python-noarch
%pycached %{python3_sitelib}/file.py


%package -n python-arched
Summary:        ...
%description -n python-arched
...
%files -n python-arched
%{python3_sitearch}/file.so


%package -n python-interpreter
Summary:        ...
%description -n python-interpreter
...
%files -n python-interpreter
%{_bindir}/python%{python3_version}


%package -n python-misplaced-library
Summary:        ...
BuildArch: noarch
%description -n python-misplaced-library
...
%files -n python-misplaced-library
%pycached /opt%{python3_sitelib}/file.py


%package -n python-misplaced-interpreter
Summary:        ...
%description -n python-misplaced-interpreter
...
%files -n python-misplaced-interpreter
/opt%{_bindir}/python%{python3_version}
