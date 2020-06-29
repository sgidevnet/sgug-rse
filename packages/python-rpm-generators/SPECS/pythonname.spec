Name:           pythonname
Version:        0
Release:        0
Summary:        ...
License:        MIT
BuildArch:      noarch

%description
...

%install
touch %{buildroot}/something
touch %{buildroot}/something_else
touch %{buildroot}/something_completely_different


%package -n python-foo
Summary:        ...
%description -n python-foo
...
%files -n python-foo
/*


%package -n python2-foo
Summary:        ...
%description -n python2-foo
...
%files -n python2-foo
/*


%package -n python3-foo
Summary:        ...
%description -n python3-foo
...
%files -n python3-foo
/*


%package -n python%{python3_version}-foo
Summary:        ...
%description -n python%{python3_version}-foo
...
%files -n python%{python3_version}-foo
/*


%package -n python3.5-foo
Summary:        ...
%description -n python3.5-foo
...
%files -n python3.5-foo
/*


%package -n ruby-foo
Summary:        ...
%description -n ruby-foo
...
%files -n ruby-foo
/*


%package -n python3-python_provide
Summary:        ...
%{?python_provide:%python_provide python3-python_provide}

%description -n python3-python_provide
...
%files -n python3-python_provide
/*


%package -n python3-py_provides
Summary:        ...
%py_provides python3-py_provides

%description -n python3-py_provides
...
%files -n python3-py_provides
/*
