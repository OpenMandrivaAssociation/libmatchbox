%define major 	1
%define libname %mklibname mb %major
%define develname %mklibname -d mb

Summary: 	Libraries for the Matchbox Desktop
Name: 		libmatchbox
Version: 	1.9
Release: 	%mkrel 4
URL: 		http://matchbox-project.org
License: 	LGPLv2+
Group: 		System/Libraries
Source0:	http://matchbox-project.org/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	X11-devel
BuildRequires:	pango-devel
BuildRequires:	png-devel
BuildRequires:	jpeg-devel
BuildRequires:	Xsettings-client-devel
Buildroot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Inter-toolkit configuration settings

%description -n %{libname}
Libraries for the Matchbox Desktop.

%package -n %{develname}
Group:          Development/C
Summary:        Static libraries and header files from %{name}
Provides:	matchbox-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	libmb-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}
Obsoletes:	%mklibname -d mb 1

%description -n %{develname}
Static libraries and header files from %{name}

%prep
%setup -q

%build
%configure2_5x --enable-xsettings --enable-png --enable-jpeg --enable-pango
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/libmb/*.h
